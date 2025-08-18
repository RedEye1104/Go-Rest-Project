import logging

from utils.Test_Frame import FrameworkUtils
from utils.Header import Hearders
from Config.Complete_URL import complete_API_URL
from utils.Create_User import CreateUser

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("checking the file.")


class TestExecute:
    user_id = None

    @staticmethod

    def test_create_user():
        # ---------------------- Step 1: Create a user ----------------------
        response = FrameworkUtils.API_Custom_Headers(
            Request_Method="POST",
            Request_URL=complete_API_URL.Post_URL(),
            Request_Headers=Hearders.GET_Header(),
            Request_json=CreateUser.create_user,
            Expected_status_code=201
        )

        TestExecute.user_id = response.json()['id']
        print(f"✅ User Created with ID: {TestExecute.user_id}")
        logger.info(f"User with ID {TestExecute.user_id} created successfully.")

        # ---------------------- Step 2: Update the user using PUT ----------------------
    @staticmethod
    def test_update_user():
        updated_user_data = {
            "name": "Updated Vishal",
            "email": "updated_vishal@example.com",
            "gender": "male",
            "status": "inactive"
        }


        put_response = FrameworkUtils.API_Custom_Headers(
            Request_Method="PUT",
            Request_URL=complete_API_URL.Put_User(TestExecute.user_id),  # URL with user_id
            Request_Headers=Hearders.GET_Header(),
            Request_json=updated_user_data,
            Expected_status_code=200
        )

        print(f"✅ PUT Response: {put_response.json()}")

        # ---------------------- Step 3: GET the updated user ----------------------

        get_response = FrameworkUtils.API_Custom_Headers(
            Request_Method="GET",
            Request_URL=complete_API_URL.Put_User(TestExecute.user_id),
            Request_Headers=Hearders.GET_Header(),
            Expected_status_code=200
        )

        user_data = get_response.json()
        print(f"✅ Updated User Fetched: {user_data}")

        # ---------------------- Step 4: Assertions ----------------------
        assert user_data['id'] == TestExecute.user_id, "User ID mismatch after update!"
        assert user_data['name'] == updated_user_data['name'], "Name not updated!"
        assert user_data['email'] == updated_user_data['email'], "Email not updated!"
        assert user_data['status'] == updated_user_data['status'], "Status not updated!"

        print("🎉 User update verified successfully!")
