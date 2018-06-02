from resources import userResources

def init_routes(api):
    api.add_resource(userResources.UserRegistration, '/registration')
    api.add_resource(userResources.UserLogin, '/login')
    api.add_resource(userResources.UserLogoutAccess, '/logout/access')
    api.add_resource(userResources.UserLogoutRefresh, '/logout/refresh')
    api.add_resource(userResources.TokenRefresh, '/token/refresh')
    api.add_resource(userResources.AllUsers, '/users')
    api.add_resource(userResources.SecretResource, '/secret')
     
