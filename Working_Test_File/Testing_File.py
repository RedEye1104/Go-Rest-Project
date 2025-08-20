import logging
import random
from utils.Test_Frame import FrameworkUtils
from utils.Header import Hearders
from Config.Complete_URL import complete_API_URL
from utils.Create_User import CreateUser



        #  *  Working on Go Rest Project
        #  1. We Create a User
        #  2. We Get The User By Created ID.
        #  3. We Update the user with that ID,
        #  4. Add some Assert for the verification
        #  5. In the end, We Delete The User.

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Testproject:
 #Set created ID None so that we can use this on later.
    created_id = None


    # ----------------------------------------------------Step:-1  Creating User----------------------------------------
    @staticmethod
    def test_create_user():
        logger.info("Start Testing the Create User Function.")
        logger.info("Creating the user with the post method.")
        post_response = FrameworkUtils.API_Custom_Headers(Request_Method="POST",
                                                          Request_URL=complete_API_URL.Post_URL(),
                                                          Request_Headers=Hearders.GET_Header(),
                                                          Request_json=CreateUser.create_user,
                                                          Expected_status_code=201
                                                          )

        logger.info("Taking ID from response body.")
        Testproject.created_id = post_response.json()['id']
        Post_response = post_response.json()
        logger.info(f"Printing response body:-    {Post_response}")
        print(f"This is the created id: :-, {Testproject.created_id}")
        logger.info(f"This is the created id: :-, {Testproject.created_id}")


    # ---------------------------------------------------Step:-2   Get User From ID-------------------------------------

    @staticmethod
    def test_get_user():
        logger.info("Start Testing the Get User Function.")
        logger.info("Getting the User Detail With The ID.")

        get_response = FrameworkUtils.API_Custom_Headers(Request_Method="GET",
                                                         Request_URL=complete_API_URL.Get_URL(Testproject.created_id),
                                                         Request_Headers=Hearders.GET_Header()
                                                         )
        logger.info(f"Get the user detail with the get method :- {get_response.json()}")
        print("This Response is getting After creating the User:-   ", get_response.json())

    # ---------------------------------------------------Step:- 3   Update User-----------------------------------------

    @staticmethod
    def test_update_user():
        logger.info("Start Testing the Update User Function.")

        email = f"vishal{random.randint(a=10000, b=99999)}@gmail.com"

        update_user_data = {
            "name": "Updated Vishal",
            "email": email,
            "gender": "male",
            "status": "inactive"
        }
        logger.info(f"This is the user updated details :- {update_user_data}")
        update_user = FrameworkUtils.API_Custom_Headers(Request_Method="PUT",
                                                        Request_URL=complete_API_URL.Put_User(Testproject.created_id),
                                                        Request_Headers=Hearders.GET_Header(),
                                                        Request_json=update_user_data,
                                                        )

        user_data = update_user.json()
        logger.info(f"Getting the user details after the update:-     {user_data}")
        print("This Response is updating the User:-   ", user_data)

    # ------------------------------------------------Step:-4  Assertions-----------------------------------------------

        assert user_data['id'] == Testproject.created_id, "User ID mismatch after update!"
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
        logger.info("After all the assert everything is working fine. it is printing the update details.")

    # --------------------------------------------------Step:- 5  Deleting user-----------------------------------------

    @staticmethod
    def test_delete_user():
        logger.info("Start Testing the Delete User Function.")

        delete_user = FrameworkUtils.API_Custom_Headers(Request_Method="DELETE",
                                                        Request_URL=complete_API_URL.delete_user(
                                                            Testproject.created_id),
                                                        Request_Headers=Hearders.GET_Header(),
                                                        Expected_status_code=204
                                                        )

        print("Status Code for Delete Request:", delete_user.status_code)
        logger.info("getting the status code to check if the user is deleted successfully!")

        if delete_user.status_code == 204:
            print(f"User with ID {Testproject.created_id} deleted successfully.")
        else:
            print("Delete request failed. Response:", delete_user.text)

        logger.info("Everything is working fine, adding this in github. ")
