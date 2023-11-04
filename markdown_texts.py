def get_main_screen_markdown():
    return """
    <div style="text-align: center">
        <h1>Cover Letter Generator</h1>
    </div>

    <div style="text-align: justify">
        <strong>Unlock the Power of Personalization!</strong> 🚀 Stand out from the crowd with a cover letter crafted just for you. 
        Our Cover Letter Generator tailors each letter to the unique details of the company, job title, your resume, and the job description. 
        Fill out the fields, hit "Generate", and witness the magic!
    </div>
    <br>
    <br>
    """

def get_sidebar_markdown():
    return """
    <div style="text-align: center">
        <h2 style="margin-bottom: 0;">Get Started with Free Monthly Credits!</h2>
    </div>
    <div  <strong>Welcome!</strong> Enjoy free calls each month on a first-come basis.
        Reach the limit? Switch to the <strong>Paid Edition</strong> (Model Choice) and input your API key 🔑.
        <br>
        <br>
        Need an API key? Get one <a href="https://openai.com/blog/openai-api" target="_blank">here</a>.<br>
        <br>
        <br>
        <br>
    </div>
    """


def get_temperature_help():
    return """
    Drag the slider to adjust the creativity of the generated text. Lower temperatures produce more predictable text, while higher values generate more creative and varied outputs.
    """