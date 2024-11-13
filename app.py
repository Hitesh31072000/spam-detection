import streamlit as st
import pickle 

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

st.title("Email Spam Classification Appliction")
st.write("This is a spam classification Appliction")

user_input = st.text_area("Enter an email to classify",height=150)
if st.button("Classify"):
    if user_input:
        data = [user_input]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)

        if pred [0]==0:
            st.success("This email is not spam")
        else:
            st.error("This email is not")
    else:
        print("please enter email")
