import streamlit as st
import requests


url = "http://127.0.0.1:8000/api/predict/"


st.title("Iris Flower Prediction")
st.write("Enter the dimensions of the flower:")


sl = st.text_input("Sepal Length", "")
sw = st.text_input("Sepal Width", "")
pl = st.text_input("Petal Length", "")
pw = st.text_input("Petal Width", "")


if st.button("Predict"):
    if sl and sw and pl and pw:
        try:
            
            payload = {
                "sl": sl,
                "sw": sw,
                "pl": pl,
                "pw": pw,
            }

            
            response = requests.post(url, data=payload)

            
            if response.status_code == 200:
                try:
                    
                    response_json = response.json()
                    prediction = response_json.get("prediction")
                    if prediction:
                        st.success(f"The predicted class is: {prediction}")
                    else:
                        st.error(f"No prediction found in the response. Response: {response_json}")
                except requests.exceptions.JSONDecodeError:
                    st.error(f"Error: Could not decode response as JSON. Response content: {response.text}")
            else:
                st.error(f"Error: Received status code {response.status_code}. Response content: {response.text}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please fill in all the input fields.")
