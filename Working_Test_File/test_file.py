
from pytest import mark
from utils.Test_Frame import FrameworkUtils
from utils.Header import Hearders
from Config.Complete_URL import complete_API_URL
from utils.Create_User import CreateUser



class TestExecute:

    @staticmethod
    @mark.update_user
    def test_update_user():
        # ---------------------- Step 1: Create a user ----------------------
        response = FrameworkUtils.API_Custom_Headers(
            Request_Method="POST",
            Request_URL=complete_API_URL.Post_URL,
            Request_Headers=Hearders.GET_Header(),
            Request_json=CreateUser.create_user,
            Expected_status_code=201
        )

        user_id = response.json()['id']
        print(f"✅ User Created with ID: {user_id}")

        # ---------------------- Step 2: Update the user using PUT ----------------------
        updated_user_data = {
            "name": "Updated Vishal",
            "email": "updated_vishal@example.com",
            "gender": "male",
            "status": "inactive"
        }

        put_response = FrameworkUtils.API_Custom_Headers(
            Request_Method="PUT",
            Request_URL=complete_API_URL.Put_User(user_id),   # URL with user_id
            Request_Headers=Hearders.GET_Header(),
            Request_json=updated_user_data,
            Expected_status_code=200
        )

        print(f"✅ PUT Response: {put_response.json()}")

        # ---------------------- Step 3: GET the updated user ----------------------
        get_response = FrameworkUtils.API_Custom_Headers(
            Request_Method="GET",
            Request_URL=complete_API_URL.Put_User(user_id),
            Request_Headers=Hearders.GET_Header(),
            Expected_status_code=200
        )

        user_data = get_response.json()
        print(f"✅ Updated User Fetched: {user_data}")

        # ---------------------- Step 4: Assertions ----------------------
        assert user_data['id'] == user_id, "User ID mismatch after update!"
        assert user_data['name'] == updated_user_data['name'], "Name not updated!"
        assert user_data['email'] == updated_user_data['email'], "Email not updated!"
        assert user_data['status'] == updated_user_data['status'], "Status not updated!"

        print("🎉 User update verified successfully!")
