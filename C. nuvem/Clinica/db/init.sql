CREATE TABLE agendamentos (
    id SERIAL PRIMARY KEY,
    paciente VARCHAR(100),
    data_agendamento DATE
);

INSERT INTO agendamentos (paciente, data_agendamento) VALUES
('João Silva', '2024-09-01'),
('Maria Oliveira', '2024-09-02'),
('Pedro Souza', '2024-09-03');
