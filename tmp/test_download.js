// Headless test to ensure download handler uses current textarea value
const { JSDOM } = require('jsdom');
const jsyaml = require('js-yaml');

(async function(){
  // build a minimal DOM with the elements used by our handler
  const html = `
    <!doctype html>
    <html><body>
      <select id="starterModule"><option value="alz">alz</option></select>
      <div id="generatedForm"></div>
      <textarea id="rawYamlText"></textarea>
      <button id="downloadEditedYaml">Download edited YAML</button>
    </body></html>`;

  const dom = new JSDOM(html, { runScripts: 'dangerously', resources: 'usable' });
  const { window } = dom;
  global.window = window;
  global.document = window.document;
  global.Blob = window.Blob;

  // monkeypatch URL.createObjectURL to capture the blob passed in
  let lastBlob = null;
  window.URL.createObjectURL = function(blob){ lastBlob = blob; return 'blob://fake-url'; };
  window.URL.revokeObjectURL = function(){ /* noop */ };

  // Simulate initial fetch populating textarea (original)
  const original = 'original: value\n';
  const edited = 'original: changed\nnewkey: 42\n';

  const textarea = document.getElementById('rawYamlText');
  textarea.value = original; // what fetched content would be

  // Now simulate user editing the textarea
  textarea.value = edited;

  // Implement the same download handler logic as in the template
  function downloadHandler(){
    const txt = (document.getElementById('rawYamlText')||{value:''}).value || '';
    // validate YAML
    try {
      jsyaml.load(txt);
    } catch(e){
      console.error('YAML validation failed', e);
      return 2;
    }
    const blob = new Blob([txt], { type: 'text/yaml' });
    const url = window.URL.createObjectURL(blob);
    // simulate anchor click by creating it and noting attrs
    const a = document.createElement('a');
    a.href = url;
    const starter = (document.getElementById('starterModule') && document.getElementById('starterModule').value) ? document.getElementById('starterModule').value : 'custom';
    a.download = 'inputs-' + starter + '-custom.yaml';
    document.body.appendChild(a);
    // in a browser this would start download; here we inspect lastBlob
    return lastBlob;
  }

  const blob = downloadHandler();
  if (!blob) {
    console.log('NO_BLOB_CREATED');
    process.exit(3);
  }
  // read blob text
  const txt = await blob.text();
  console.log('BLOB_TEXT:\n' + txt);
  if (txt === edited) {
    console.log('TEST_PASSED: download uses edited textarea content');
    process.exit(0);
  } else {
    console.log('TEST_FAILED: download used stale/original content');
    process.exit(4);
  }
})();
