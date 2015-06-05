# from django.test import SimpleTestCase, Client
# from models.post import Post
# from models.busline import Busline

# STATUS_OK = 200
# STATUS_REDIRECT = 302


# class PostControllerTest(SimpleTestCase):

#     def setUp(self):
#         self.client = Client()

#     def setup(busline)
#     def create_post(self):
#     	post.comment ='hello world'
#         post.position = 'position'
#     	post.traffic = 2
#     	post.capacity = 2
#     	post.terminals = ['terminals']
#     	post.date = ['date']
#     	post.time = ['time']
#     	post.save()

#     def test_register_post(self):
#         response = self.client.get("/realizar_post/")
#         self.assertEquals(response.status_code, STATUS_REDIRECT)

#     def test_register_post_sucess_db(self):
#     	data=self.register_post_data()
#     	dbbefore=User.objects.all().conut()
#     	self.client.post('save_post/',data)
#     	db_after=User.objects.all().count()
#     	self.asserTrue(db_after>db_before)
