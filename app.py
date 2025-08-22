from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wizard')
def wizard():
    return render_template('wizard.html')


@app.route('/get-started')
def get_started():
    return render_template('get_started.html')

# Phase 0
@app.route('/phase0')
def phase0():
    return render_template('phases/phase0.html')

# Phase 1 sub-phases
@app.route('/phase1/tools')
def phase1_tools():
    return render_template('phases/phase1_tools.html')

@app.route('/phase1/subscriptions')
def phase1_subscriptions():
    return render_template('phases/phase1_subscriptions.html')

@app.route('/phase1/vcs')
def phase1_vcs():
    return render_template('phases/phase1_vcs.html')

# Phase 2
@app.route('/phase2')
def phase2():
    return render_template('phases/phase2.html')

# Phase 2 flow pages
@app.route('/phase2/terraform-azuredevops')
def phase2_terraform_azuredevops():
    return render_template('phases/terraform-azuredevops.html')

@app.route('/phase2/terraform-github')
def phase2_terraform_github():
    return render_template('phases/terraform-github.html')

# Phase 3
@app.route('/phase3')
def phase3():
    return render_template('phases/phase3.html')


@app.route('/finish')
def finish():
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True)
