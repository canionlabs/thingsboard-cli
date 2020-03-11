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