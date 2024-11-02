Salut ! Aceasta este primul proiect pe care il postez aici . 
Totodata este si prima tema de la facultate . 
Am creat un cod care genereaza un cod qr si care , atunci cand este scanat cauta pe google "Tema facuta de Iancu Andrei"
Am folosit biblioteca care permite generarea codurilor
In data am retinut mesajul care va fi afisat in urma scanarii
Am creat un obiect qr cu versiunea 1 ( 21x21 patratele , cea mai mica versiune) ,
am stabilit nivelul de corectie al erorilor sa fie L , cea mai mica protectie ,
dimensiunea de 10 pixeli si grosimea codului de 4 patratele 
Dupa aceea am adaugat datele de mai sus in obiectul qr pentru a fi 
codificata in structura codului QR
"qr.make(fit=true)" pentru a ajusta automat dimensiunea 
Prin " img=qr.make_image.. " am generat imaginea codului qr , patratelele fiind negre iar culoarea
de background fiind alba ; Dupa aceea am salvat imaginea cu denumirea "codqr.png"
La final am adaugat un mesaj de final care sa confirme ca imaginea a fost generata cu succes 

Va multumesc pentru atentie ! 
P.S : La data postarii acestui cod ( 02.11.2024) inca sunt incepator si experimentez
platforma GITHUB si Python .
