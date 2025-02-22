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

    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)
);

-- insert some values
INSERT INTO clientes (nome, email, telefone, endereco) VALUES
    ('Luiza', 'lula@gmail.com', '999999999', 'Cocal, rua 3'),
    ('Vitor', 'vitorpcrcanedo@gmail.com', '777777777', 'itaparica, av champanhar'),
    ('Lucas', 'lucasdlima@gmail.com', '222222222', 'ibes, proximo a pracinha');
