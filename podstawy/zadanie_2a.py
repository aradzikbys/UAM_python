"""
Poniżej znajduje się lista `websites`. 
 * Pod jakim indeksem znajduje się wartość 'pinterest.com'?
 * Zamień wartość piątego elementu na 'yahoo.com'.
 * Dodaj na koniec listy nowy element: 'bing.com'
 * Korzytając z indeksowania stwórz podlistę składającą się z elementów 'facebook.com', 'twitter.com'. Wynik przypisz do zmniennej `social_networks`.
 * Rozszesz listę `websites` o elementy z listy `polish_websites`.
 * Ile elementów liczy teraz lista `websites`?
"""
websites = ['google.com', 'facebook.com', 'twitter.com', 'pinterest.com', 'python.org']
polish_websites = ['onet.pl', 'interia.pl', 'wp.pl']

#A:
websites.index('pinterest.com')

#B
websites[4] = 'yahoo.com'
print(websites)

#C
websites.append('bing.com')
print(websites)

#D
social_networks = websites[1:3]
print(social_networks)

#E
websites = websites + polish_websites
print(websites)

#F
print(len(websites))