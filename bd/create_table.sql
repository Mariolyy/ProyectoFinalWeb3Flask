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


insert into estadostarea(id, nombre) VALUES(1, 'TERMINADO'); 
insert into estadostarea(id, nombre) VALUES(2, 'EN PROCESO'); 
insert into estadostarea(id, nombre) VALUES(3, 'ELIMINADO'); 

insert into TiposProyecto(id, nombre) values(1, 'GRANDE');
insert into TiposProyecto(id, nombre) values(2, 'MEDIANO');
insert into TiposProyecto(id, nombre) values(3, 'PEQUEÑO');

insert into Proyectos(id, nombre, ubicacion, cliente_id, tipo_proyecto_id) 
values(1, 'Mall Gran via', 'Zona San Pedro, calle D', 1, 1);

insert into Tareas (id, proyecto_id, nombre, fecha_inicio, fecha_fin, estado_id)
values(1, 1, 'Muro de contencion', date('2025-01-01'), date('2025-05-10'), 1);
insert into Tareas (id, proyecto_id, nombre, fecha_inicio, fecha_fin, estado_id)
values(2, 1, 'Muro perimetral', date('2025-02-10'), date('2025-03-10'), 1);
