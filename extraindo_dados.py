from dados_repos import DadosRepositorios

amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens() 
print(f'A Amazon possuí {len(ling_mais_usadas_amzn)} repositórios.')

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens() 
print(f'A Netflix possuí {len(ling_mais_usadas_netflix)} repositórios.')

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()
print(f'O Spotify possuí {len(ling_mais_usadas_spotify)} repositórios.')

apple_rep = DadosRepositorios('apple')
ling_mais_usadas_apple = apple_rep.cria_df_linguagens()
print(f'A Apple possuí {len(ling_mais_usadas_spotify)} repositórios.')


# salvando os dados
ling_mais_usadas_amzn.to_csv('dados/linguagens_amazon.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv')

print('='*30)
print('Salvamento Concluído')
print('='*30)