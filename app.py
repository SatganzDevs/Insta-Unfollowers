import instaloader
import streamlit as st

# Initialize instaloader
L = instaloader.Instaloader()

st.title('Instagram Unfollowers List')
st.subheader('This web is created by Kurniawan Satria, and is 100% safe.')

# Get the target username from the user
username = st.text_input('Instagram Username to Check:')

# Display button to start the process
if st.button('Check Unfollowers'):
    try:
        # Login using the preset account
        L.login("siestanatsugani", "jayayusman1")
        st.success("Login successful! Checking unfollowers for the given username.")

        # Get the profile information of the target username
        profile = instaloader.Profile.from_username(L.context, username)

        # Get the list of users the target profile follows
        following = set(profile.get_followees())

        # Get the list of users who follow the target profile
        followers = set(profile.get_followers())

        # Get the list of users who don't follow the target profile back
        non_followers = following - followers

        if len(non_followers) == 0:
            st.success("No users who don't follow you back.")
        else:
            # Display the list of users who don't follow you back
            st.warning("Users who don't follow you back:")
            for user in non_followers:
                st.markdown(f"<span style='color:blue'>{user.username}</span>", unsafe_allow_html=True)

        # Logout from Instagram account
        L.close()

    except instaloader.exceptions.ConnectionException:
        st.error("Connection error occurred. Please check your internet connection and try again.")
    except instaloader.exceptions.BadCredentialsException:
        st.error("Login failed for the preset account. Please check the login details.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        st.error("Two-factor authentication is required for the preset account.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
