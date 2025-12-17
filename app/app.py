"""
Sistema de Gestión de Construcción - Flask App
Versión Corregida para tu Base de Datos
"""
from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

# Añadir carpeta controller al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'controller'))

app = Flask(__name__)
app.secret_key = 'clave_secreta_construccion_2024'

# ==================== IMPORTACIÓN SEGURA ====================

# Intenta importar los controladores
try:
    from controllerProyectos import listaProyecto, insertarProyecto, obtenerTiposProyecto, obtenerProyectoPorId, actualizarProyecto, eliminarProyecto
    print("✅ Controladores importados correctamente")
except ImportError as e:
    print(f"⚠️ Error importando controladores: {e}")
    # Funciones de respaldo
    def listaProyecto(): return []
    def insertarProyecto(*args): return 1
    def obtenerTiposProyecto(): 
        return [
            {"id": 1, "nombre": "Residencial"},
            {"id": 2, "nombre": "Comercial"},
            {"id": 3, "nombre": "Industrial"},
            {"id": 4, "nombre": "Infraestructura"}
        ]

# ==================== RUTAS PRINCIPALES ====================

@app.route('/')
def inicio():
    """Página de inicio"""
    proyectos = listaProyecto()
    return render_template('public/index.html', proyectos=proyectos)

# ==================== RUTAS PARA PROYECTOS ====================

@app.route('/proyectos')
def listar_proyectos():
    """Lista todos los proyectos"""
    try:
        # Obtener proyectos desde la base de datos
        proyectos = listaProyecto()
        
        # Contar por estado (simulado por ahora)
        estados_count = {
            'En Progreso': len([p for p in proyectos if p.get('estado') == 'En Progreso']),
            'Planificado': len([p for p in proyectos if p.get('estado') == 'Planificado']),
            'Completado': len([p for p in proyectos if p.get('estado') == 'Completado']),
            'Suspendido': 0,
            'Cancelado': 0
        }
        
        return render_template('public/listarProyectos.html', 
                             proyectos=proyectos,
                             total=len(proyectos),
                             estados_count=estados_count)
                             
    except Exception as e:
        print(f"Error: {e}")
        flash('Error al cargar proyectos', 'danger')
        return render_template('public/listarProyectos.html', 
                             proyectos=[], 
                             total=0,
                             estados_count={'En Progreso': 0, 'Planificado': 0, 'Completado': 0})

@app.route('/proyectos/agregar', methods=['GET', 'POST'])
def agregar_proyecto():
    """Agrega un nuevo proyecto"""
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form.get('nombre', '').strip()
            ubicacion = request.form.get('ubicacion', '').strip()
            tipo_id = request.form.get('tipo_proyecto', 1, type=int)  # Ahora recibe el ID directamente
            
            # Validar
            if not nombre:
                flash('❌ El nombre es requerido', 'danger')
                return redirect(url_for('agregar_proyecto'))
            
            if not ubicacion:
                flash('❌ La ubicación es requerida', 'danger')
                return redirect(url_for('agregar_proyecto'))
            
            # Insertar en BD (tipo_id ya viene del formulario)
            nuevo_id = insertarProyecto(nombre, ubicacion, tipo_id)
            
            if nuevo_id > 0:
                flash(f'✅ Proyecto "{nombre}" agregado correctamente', 'success')
                return redirect(url_for('listar_proyectos'))
            else:
                flash('❌ Error al guardar el proyecto', 'danger')
                
        except Exception as e:
            flash(f'❌ Error: {str(e)}', 'danger')
    
    # GET: Mostrar formulario
    tipos = obtenerTiposProyecto()
    
    return render_template('public/agregarProyecto.html', 
                         tipos_proyecto=tipos)

@app.route('/proyectos/editar/<int:id>', methods=['GET', 'POST'])
def editar_proyecto(id):
    """Edita un proyecto"""
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form.get('nombre', '').strip()
            ubicacion = request.form.get('ubicacion', '').strip()
            tipo_proyecto = request.form.get('tipo_proyecto', 'Residencial')
            
            # Validar
            if not nombre:
                flash('❌ El nombre es requerido', 'danger')
                return redirect(url_for('editar_proyecto', id=id))
            
            if not ubicacion:
                flash('❌ La ubicación es requerida', 'danger')
                return redirect(url_for('editar_proyecto', id=id))
            
            # Obtener ID del tipo
            tipos = obtenerTiposProyecto()
            tipo_id = 1  # Por defecto
            
            for tipo in tipos:
                if tipo['nombre'] == tipo_proyecto:
                    tipo_id = tipo['id']
                    break
            
            # Actualizar en BD
            resultado = actualizarProyecto(id, nombre, ubicacion, tipo_id)
            
            if resultado:
                flash(f'✅ Proyecto "{nombre}" actualizado correctamente', 'success')
                return redirect(url_for('listar_proyectos'))
            else:
                flash('❌ Error al actualizar el proyecto', 'danger')
                
        except Exception as e:
            flash(f'❌ Error: {str(e)}', 'danger')
    
    # GET: Mostrar formulario con datos del proyecto
    proyecto = obtenerProyectoPorId(id)
    
    if not proyecto:
        flash('❌ Proyecto no encontrado', 'danger')
        return redirect(url_for('listar_proyectos'))
    
    tipos = obtenerTiposProyecto()
    tipos_nombres = [tipo['nombre'] for tipo in tipos]
    
    return render_template('public/editarProyecto.html', 
                         proyecto=proyecto,
                         tipos_proyecto=tipos_nombres)

@app.route('/proyectos/eliminar/<int:id>')
def eliminar_proyecto(id):
    """Elimina un proyecto"""
    try:
        resultado = eliminarProyecto(id)
        
        if resultado:
            flash(f'🗑️ Proyecto ID {id} eliminado correctamente', 'success')
        else:
            flash(f'❌ No se pudo eliminar el proyecto ID {id}', 'danger')
            
    except Exception as e:
        flash(f'❌ Error al eliminar: {str(e)}', 'danger')
    
    return redirect(url_for('listar_proyectos'))

# ==================== RUTAS PARA TAREAS ====================

@app.route('/tareas')
def listar_tareas():
    """Lista tareas"""
    tareas = [
        {
            'id': 1,
            'nombre': 'Cimentación',
            'proyecto': 'Edificio Torres del Norte',
            'fecha_inicio': '2024-01-15',
            'fecha_fin': '2024-02-15',
            'estado': 'Completada',
            'prioridad': 'Alta'
        }
    ]
    
    return render_template('public/listarTareas.html',
                         tareas=tareas,
                         total=len(tareas))

@app.route('/tareas/agregar')
def agregar_tarea():
    """Agrega tarea"""
    proyectos = listaProyecto()
    proyectos_select = [{'id': p['id'], 'nombre': p.get('proyecto', 'Sin nombre')} for p in proyectos]
    
    if not proyectos_select:
        proyectos_select = [{'id': 1, 'nombre': 'Proyecto de ejemplo'}]
    
    return render_template('public/agregarTarea.html',
                         proyectos=proyectos_select,
                         estados=['Pendiente', 'En Progreso', 'Completada'],
                         prioridades=['Alta', 'Media', 'Baja'])

# ==================== RUTAS PARA ESTADOS ====================

@app.route('/estados-tarea')
def listar_estados():
    """Lista estados"""
    estados = [
        {'id': 1, 'nombre': 'Pendiente', 'color': 'warning'},
        {'id': 2, 'nombre': 'En Progreso', 'color': 'primary'},
        {'id': 3, 'nombre': 'Completada', 'color': 'success'},
        {'id': 4, 'nombre': 'Atrasada', 'color': 'danger'}
    ]
    
    return render_template('public/listarEstadosTareas.html',
                         estados=estados,
                         total=len(estados))

# ==================== EJECUCIÓN ====================

if __name__ == '__main__':
    print("=" * 50)
    print("🏗️  SISTEMA DE GESTIÓN DE CONSTRUCCIÓN")
    print("=" * 50)
    print("\n🌐 Servidor: http://localhost:8000")
    print("\n📍 Rutas principales:")
    print("   /               - Inicio")
    print("   /proyectos      - Lista proyectos")
    print("   /proyectos/agregar - Agregar proyecto")
    print("   /tareas         - Lista tareas")
    print("   /estados-tarea  - Lista estados")
    print("\n" + "=" * 50)
    
    app.run(debug=True, port=8000, host='127.0.0.1')