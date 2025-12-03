-- Crear tabla TiposProyecto
CREATE TABLE TiposProyecto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla EstadosTarea
CREATE TABLE EstadosTarea (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla Proyectos
CREATE TABLE Proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    ubicacion VARCHAR(200),
    cliente_id INT NOT NULL,
    tipo_proyecto_id INT NOT NULL,
    CONSTRAINT fk_proyecto_tipo
        FOREIGN KEY (tipo_proyecto_id) REFERENCES TiposProyecto(id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Crear tabla Tareas
CREATE TABLE Tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    proyecto_id INT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    estado_id INT NOT NULL,
    CONSTRAINT fk_tarea_proyecto
        FOREIGN KEY (proyecto_id) REFERENCES Proyectos(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_tarea_estado
        FOREIGN KEY (estado_id) REFERENCES EstadosTarea(id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);
