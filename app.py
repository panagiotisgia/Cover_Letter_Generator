import streamlit as st
#import openai
from markdown_texts import *
from llm_cover_letter import *



def main():

    # Main screen 
    st.markdown(get_main_screen_markdown(), unsafe_allow_html=True)

    # Inputs
    company_name = st.text_input("Company Name", placeholder = 'Insert company name here ...')
    job_title = st.text_input("Job Title", placeholder = 'Insert job position here ...')
    uploaded_cv = st.file_uploader("Upload your CV", type=['pdf'])
    job_description = st.text_area("Job Description", height=300, placeholder = 'Insert the job description here ...' )
    temperature = st.slider("Creativity Level (Temperature)", min_value=0.0, max_value=1.0, value=0.7, step=0.01,
                        help=get_temperature_help())

    # Side bar
    st.sidebar.markdown(get_sidebar_markdown(), unsafe_allow_html=True)  
    edition = st.sidebar.radio("Select Option", ["Free Edition", "Paid Edition"])

    # Depending on the edition, show model options
    model_option = None
    if edition == "Paid Edition":
        model_option = st.sidebar.selectbox("Choose Model", ["GPT-4", "GPT-3.5", "GPT-3"])
    
    # Check inputs are filled
    all_inputs_filled = company_name and job_title and uploaded_cv and job_description
    correct_file_uploaded = uploaded_cv is not None and uploaded_cv.type == "application/pdf"

    # Generate button
    generate_button = st.button("Generate")

    # Init an empty message container for success/error messages
    message = st.empty()


    ##### Free Edition Logic  #####
    if edition == "Free Edition":
        if generate_button:

            # Check if the fields are filled
            if all_inputs_filled and correct_file_uploaded:  

                try: 
                    with st.spinner('Generating your cover letter...'):
                        # Get the answer
                        answer = free_edition_llm(company_name, job_title, uploaded_cv, job_description, temperature).replace('\n', '').replace('\t', '')
                        
                        # Clear the message placeholder before displaying the success message
                        message.empty()
                        message.success('Cover letter generation completed!')
                        st.text_area("Cover Letter", answer, height=300)
                
                except openai.error.AuthenticationError as e:
                    st.error(e)
                except openai.error.APIError as e:
                    st.error(e)
                except openai.error.Timeout as e:
                    st.error(e)
                except openai.error.RateLimitError as e:
                    st.error(e)
                except openai.error.APIConnectionError as e:
                    st.error(e)
                except openai.error.InvalidRequestError  as e:
                    st.error(e)
                except openai.error.ServiceUnavailableError as e:
                    st.error(e)
                
            else:
                st.error("Please fill in all fields and upload a PDF file to generate the cover letter.")
                
    ###### Paid Edition Logic #####
    elif edition == "Paid Edition":
        api_key = st.sidebar.text_input("Open API Key", type="password")
        
        if generate_button:
            if all_inputs_filled and correct_file_uploaded and api_key:
                # Assuming you'll use company_name, job_title, uploaded_cv, job_description, and api_key in your generation logic
                answer = 'Great cover letter'  # Here you would call your function to generate the cover letter
                st.text_area("Cover Letter", answer, height=300)
            else:
                error_message = "Please enter your OpenAI API key." if not api_key else "Please fill in all fields and upload a PDF file to generate the cover letter."
                st.error(error_message)






if __name__ == "__main__":
    main()