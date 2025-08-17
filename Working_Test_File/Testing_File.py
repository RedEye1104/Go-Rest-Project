import random
from utils.Test_Frame import FrameworkUtils
from utils.Header import Hearders
from Config.Complete_URL import complete_API_URL
from utils.Create_User import CreateUser


class Testproject:

    # ----------------------------------------------------Step:-1  Creating User---------------------------------------------
    @staticmethod
    def test_go_rest():
        post_response = FrameworkUtils.API_Custom_Headers(Request_Method="POST",
                                                          Request_URL=complete_API_URL.Post_URL(),
                                                          Request_Headers=Hearders.GET_Header(),
                                                          Request_json=CreateUser.create_user,
                                                          Expected_status_code=201
                                                          )

        created_id = post_response.json()['id']
        print(f"This is the created id: :-, {created_id}")

        # -----------------------------------------------Step:-2   Get User From ID-------------------------------------

        get_response = FrameworkUtils.API_Custom_Headers(Request_Method="GET",
                                                         Request_URL=complete_API_URL.Get_URL(created_id),
                                                         Request_Headers=Hearders.GET_Header()
                                                         )

        print("This Response is getting After creating the User:-   ", get_response.json())


        # -----------------------------------------------Step:- 3   Update User-----------------------------------------

        email = f"vishal{random.randint(a=10000 , b=99999 )}@gmail.com"

        update_user_data = {
        "name": "Updated Vishal",
        "email": email,
        "gender": "male",
        "status": "inactive"
        }

        update_user = FrameworkUtils.API_Custom_Headers(Request_Method="PUT",
                                                    Request_URL=complete_API_URL.Put_User(created_id),
                                                    Request_Headers=Hearders.GET_Header(),
                                                    Request_json=update_user_data,
                                                    )

        user_data = update_user.json()
        print("This Response is updating the User:-   ", user_data)


#---------------------------------------------------------Step:-4  Assertions-------------------------------------------


        assert user_data['id'] == created_id, "User ID mismatch after update!"
        print("User ID is matched after update!")

        assert user_data['name'] == update_user_data['name'], "Name not updated!"
        print("Name is matched after update!")

        assert user_data['email'] == update_user_data['email'], "Email mismatch after update!"
        print("Email is matched after update!")

        assert user_data['gender'] == update_user_data['gender'], "Gender mismatch after update!"
        print("Gender is matched after update!")

        assert user_data['status'] == update_user_data['status'], "Status mismatch after update!"
        print("Status is matched after update!")

        print("🎉 User update verified successfully!")


#-----------------------------------------------------------Step:- 5  Deleting user-------------------------------------

        delete_user = FrameworkUtils.API_Custom_Headers(Request_Method="DELETE",
                                                        Request_URL=complete_API_URL.delete_user(created_id),
                                                        Request_Headers=Hearders.GET_Header(),
                                                        Expected_status_code=204
                                                        )

        print("Status Code for Delete Request:", delete_user.status_code)

        if delete_user.status_code == 204:
            print(f"User with ID {created_id} deleted successfully.")
        else:
            print("Delete request failed. Response:", delete_user.text)