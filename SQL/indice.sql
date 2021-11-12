CREATE INDEX cidadex ON public.localizacao USING btree (cidade);

--Usuários que fizeram avaliação de negócios em Los Angeles
Explain Analyze SELECT * FROM public.usuario WHERE id IN
(SELECT id_usuario FROM public.avaliacao WHERE avaliacao.id_comercio IN 
(SELECT id_comercio FROM public.localizacao WHERE cidade = 'Los Angeles'))
