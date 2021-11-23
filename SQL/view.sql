CREATE OR REPLACE VIEW "10 Melhores Comercios por Avaliacao" AS
SELECT comercio.nome, comercio.preco, avg(avaliacao.nota) FROM public.comercio
INNER JOIN public.avaliacao ON comercio.id = avaliacao.id_comercio
GROUP BY comercio.nome, comercio.preco ORDER BY avg(avaliacao.nota) DESC
LIMIT 10;

SELECT * FROM "10 Melhores Comercios por Avaliacao";

