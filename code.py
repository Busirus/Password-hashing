import hashlib

def hash_password(password, salt=None, algorithm='md5'):
    # Convertir le mot de passe en chaîne de caractères UTF-8
    password = str(password).encode('utf-8')

    # Si un sel est fourni, le concaténer au mot de passe
    if salt:
        password = password + str(salt).encode('utf-8')

    # Hacher le mot de passe en utilisant l'algorithme spécifié
    if algorithm == 'md5':
        hashed_password = hashlib.md5(password).hexdigest()
    elif algorithm == 'sha1':
        hashed_password = hashlib.sha1(password).hexdigest()
    elif algorithm == 'mysql':
        hashed_password = '*' + hashlib.sha1(password).hexdigest().upper()
    elif algorithm == 'ntlm':
        hashed_password = hashlib.new('md4', password).hexdigest()
    elif algorithm == 'sha256':
        hashed_password = hashlib.sha256(password).hexdigest()
    elif algorithm == 'sha512':
        hashed_password = hashlib.sha512(password).hexdigest()
    return hashed_password

# Demander à l'utilisateur d'entrer un mot de passe
password = input('Entrez un mot de passe : ')

# Demander à l'utilisateur de choisir un algorithme de hachage

algorithm = input('Choisissez un algorithme de hachage (md5, sha1, mysql, ntlm, sha256, sha512) : ')

# Verifier que l'algorithme choisi est valide
while algorithm not in ('md5', 'sha1', 'mysql', 'ntlm', 'sha256', 'sha512'):
    algorithm = input('Algorithme de hachage non valide. Veuillez choisir un algorithme de hachage (md5, sha1, mysql, ntlm, sha256, sha512) : ')
 
    # Demander à l'utilisateur s'il souhaite ajouter un sel au mot de passe
salt = input('Entrez un sel pour le mot de passe (facultatif) : ')
  
    # Hacher le mot de passe en utilisant l'algorithme et le sel choisi par l'utilisateur
hashed_password = hash_password(password, salt, algorithm)

    # Afficher le mot de passe haché
print('Mot de passe haché :', hashed_password)

 
 
 