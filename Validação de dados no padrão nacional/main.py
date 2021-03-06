from ValidDocument import Document
from ValidPhone import ValidPhone
from SearchAddress import SearchAddress
from DatasBr import DatasBr


example_cpf = "15316264754"
cpf = Document.create_document(example_cpf)
print(cpf)

example_cnpj = "35379838000112"
cnpj = Document.create_document(example_cnpj)
print(cnpj)

telephone = "552126481234"
telephone_object = ValidPhone(telephone)
print(telephone_object)

date_today = DatasBr()
print(date_today)

date_today.registration_moment_difference()


cep = "21721022"
cep_object = SearchAddress(cep)
bairro, cidade, uf = cep_object.access_zip_code()
print(bairro, cidade, uf)

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1)
# print(hoje)
# print(amanha)
#
# print(hoje - amanha)