#receber uma linha de comando

#fazer o tratamento dessa entrada, ex: "thingsboard create-group --name:victor"
# cli = input('Entre com o comando: ')

# if("create-group" in cli.split(' ')):
#     self.createGroup()

#sequência de criação:
# 1- criar uma grupo -> /api/entityGroup 
# params: {
#   "additionalInfo": "string",
#   "configuration": "string",
#   "createdTime": 0,
#   "groupAll": true,
#   "id": {
#     "id": "string"
#   },
#   "name": "string",
#   "ownerId": {
#     "entityType": "TENANT",
#     "id": "string"
#   },
#   "ownerIds": [
#     {
#       "entityType": "TENANT",
#       "id": "string"
#     }
#   ],
#   "type": "CUSTOMER"
# }

# 2 - criar um customer -> /api/customer{?entityGroupId}
# params: {
#   "additionalInfo": "string",
#   "address": "string",
#   "address2": "string",
#   "city": "string",
#   "country": "string",
#   "createdTime": 0,
#   "customerId": {
#     "id": "string"
#   },
#   "email": "string",
#   "id": {
#     "id": "string"
#   },
#   "name": "string",
#   "ownerId": {
#     "entityType": "TENANT",
#     "id": "string"
#   },
#   "parentCustomerId": {
#     "id": "string"
#   },
#   "phone": "string",
#   "state": "string",
#   "tenantId": {
#     "id": "string"
#   },
#   "title": "string",
#   "zip": "string"
# }

# 3 - criar um user dentro do customer -> /api/user{?sendActivationMail,entityGroupId}
# params: {
#   "additionalInfo": "string",
#   "authority": "SYS_ADMIN",
#   "createdTime": 0,
#   "customerId": {
#     "id": "string"
#   },
#   "email": "string",
#   "firstName": "string",
#   "id": {
#     "id": "string"
#   },
#   "lastName": "string",
#   "name": "string",
#   "ownerId": {
#     "entityType": "TENANT",
#     "id": "string"
#   },
#   "tenantId": {
#     "id": "string"
#   }
# }

# 4 - dar permissão para esse usuario -> /api/permissions/allowedPermissions
# params: {
#   "allowedForGroupOwnerOnlyGroupOperations": [
#     "ALL"
#   ],
#   "allowedForGroupOwnerOnlyOperations": [
#     "ALL"
#   ],
#   "allowedForGroupRoleOperations": [
#     "ALL"
#   ],
#   "allowedResources": [
#     "ALL"
#   ],
#   "operationsByResource": {},
#   "userOwnerId": {
#     "entityType": "TENANT",
#     "id": "string"
#   },
#   "userPermissions": {
#     "genericPermissions": {},
#     "groupPermissions": {},
#     "readGroupPermissions": {}
#   }
# }

# 5 - criar o device -> /api/device{?accessToken,entityGroupId}
# params: {
#   "additionalInfo": "string",
#   "createdTime": 0,
#   "customerId": {
#     "id": "string"
#   },
#   "id": {
#     "id": "string"
#   },
#   "label": "string",
#   "name": "string",
#   "ownerId": {
#     "entityType": "TENANT",
#     "id": "string"
#   },
#   "tenantId": {
#     "id": "string"
#   },
#   "type": "string"
# }

# 6 - criar dashboard -> /api/dashboard{?entityGroupId}
# params: {
#   "assignedCustomers": [
#     {
#       "customerId": {
#         "id": "string"
#       },
#       "public": true,
#       "title": "string",
#       "isPublic": true
#     }
#   ],
#   "configuration": "string",
#   "createdTime": 0,
#   "customerId": {
#     "id": "string"
#   },
#   "id": {
#     "id": "string"
#   },
#   "name": "string",
#   "ownerId": {
#     "entityType": "TENANT",
#     "id": "string"
#   },
#   "tenantId": {
#     "id": "string"
#   },
#   "title": "string"
# }