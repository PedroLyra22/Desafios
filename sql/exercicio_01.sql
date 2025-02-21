-- create a table
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
);

CREATE TABLE IF NOT EXISTS filmes (
    id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    ano_lancamento INTEGER,
    disponivel BOOLEAN
);

CREATE TABLE IF NOT EXISTS locacoes (
    id_locacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_filme INTEGER NOT NULL,
    data_locacao DATE NOT NULL,
    data_devolucao DATE,
    status_locacao VARCHAR(10) CHECK (status_locacao IN ('ativo', 'concluido'))
);