CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY,
    produto TEXT NOT NULL CHECK (length(trim(produto)) > 0),
    qtd INTEGER NOT NULL DEFAULT 0 CHECK (qtd >=0),
    data_entrada TEXT NOT NULL DEFAULT (DATE('now')),
    valor_unidade INTEGER NOT NULL CHECK (valor_unidade >= 0)
);


