import streamlit as st


# Mocked constants. Adjust accordingly.
COMMUNITY_CREDITS_PER_DAY = 10
used_credits_today = 0  # You'd have to track and update this value in a real-world scenario.



def main():

    #st.title('Cover Letter Generator')
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )
    
    # Inputs
    company_name = st.text_input("Company Name", placeholder = 'Insert company name here ...')
    job_title = st.text_input("Job Title", placeholder = 'Insert job position here ...')
    uploaded_cv = st.file_uploader("Upload your CV", type=['pdf'])
    job_description = st.text_area("Job Description", height=300,placeholder = 'Insert the job description here ...' )

    st.sidebar.markdown(
        """
        <div style="text-align: center">
            <h2 style="margin-bottom: 0;">Get Started with Free Monthly Credits!</h2>
        </div>
        <div  <strong>Welcome!</strong> Enjoy free calls each month on a first-come basis.
            Reach the limit? Switch to the <strong>Paid Edition</strong> and input your API key.
            <br>
            <br>
            Need an API key? Get one <a href="https://openai.com/blog/openai-api" target="_blank">here</a>.<br>
            <br>
            <br>
            <br>
        </div>
        """,
        unsafe_allow_html=True
    )
    #title_ed = st.title("Select Edition")
    edition = st.sidebar.radio("Select Option", ["Free Edition", "Paid Edition"])
    

    # Free Edition Logic
    if edition == "Free Edition":
        
        global used_credits_today

        # Check if credits are available
        if used_credits_today < COMMUNITY_CREDITS_PER_DAY:
            api_key = "YOUR_PERSONAL_API_KEY"

            if st.button("Generate"):
                # Assuming you'll use company_name, job_title, uploaded_cv, and job_description in your generation logic
                answer = 'Great cover letter'   # generate_answer(api_key, company_name, job_title, uploaded_cv, job_description)
                st.text_area("Text box 3: Answer", answer)

                used_credits_today += 1
        else:
            st.warning("Sorry, daily community credits are exhausted. Please switch to the Paid Edition.")

    # Paid Edition Logic
    elif edition == "Paid Edition":
        api_key = st.sidebar.text_input("Open API Key", type="password")

        if st.button("Generate"):
            if not api_key:
                st.warning("Please enter your OpenAI API key!")
            else:
                # Assuming you'll use company_name, job_title, uploaded_cv, and job_description in your generation logic
                answer = 'Great cover letter'   # generate_answer(api_key, company_name, job_title, uploaded_cv, job_description)
                st.text_area("Text box 3: Answer", answer)

if __name__ == "__main__":
    main()