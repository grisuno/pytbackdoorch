# ============================================================================
# Makefile para loader.cpp (backdoor .pth en C++ con LibTorch)
# ============================================================================
# Uso:
#   make                # Compila loader.cpp en ejecutable 'loader_cpp'
#   make clean          # Elimina objetos y ejecutables
#   make run            # Compila y ejecuta (requiere que el listener esté activo)
#   make TORCH_DIR=/ruta/personalizada  # Especifica directorio de LibTorch
# ============================================================================

# ----------------------------------------------------------------------------
# 1. DETECCIÓN Y CONFIGURACIÓN DE LIBTORCH
# ----------------------------------------------------------------------------
# Si no se define TORCH_DIR, se intenta usar la variable de entorno.
# Si no está definida, se asume una ruta común (/usr/local/libtorch).
# Para sistemas con múltiples versiones, se recomienda definir explícitamente.
TORCH_DIR ?= $(shell echo $$TORCH_DIR)
ifeq ($(TORCH_DIR),)
    TORCH_DIR := /usr/local/libtorch
endif

# Verificar que el directorio existe
ifeq ($(wildcard $(TORCH_DIR)),)
    $(warning TORCH_DIR='$(TORCH_DIR)' no existe. Por favor, establece TORCH_DIR correctamente.)
    $(warning Ejemplo: make TORCH_DIR=/opt/libtorch-cpu)
endif

# ----------------------------------------------------------------------------
# 2. COMPILADOR Y FLAGS
# ----------------------------------------------------------------------------
CXX := g++
# Estándar C++17 es requerido por LibTorch (para variantes, filesystem, etc.)
CXXFLAGS := -std=c++17 -O2 -Wall -Wextra -pthread
# Flags de inclusión: apuntan a los directorios include de LibTorch
CXXFLAGS += -I$(TORCH_DIR)/include -I$(TORCH_DIR)/include/torch/csrc/api/include

# ----------------------------------------------------------------------------
# 3. ENLACE (LDFLAGS)
# ----------------------------------------------------------------------------
# Directorio de bibliotecas
LDFLAGS := -L$(TORCH_DIR)/lib

# Bibliotecas necesarias para LibTorch (orden importante)
# -ltorch: núcleo de la biblioteca
# -lc10: biblioteca de utilidades (tensores, etc.)
# -ltorch_cpu: implementación CPU (si se usa versión CPU)
# -lc10_cuda: si se usa CUDA (opcional, comentar si no)
# Además se necesitan librerías del sistema: pthread, dl, c++abi, etc.
LDLIBS := -ltorch -lc10 -ltorch_cpu
# Para versiones con CUDA, descomentar la siguiente línea y comentar la anterior
# LDLIBS := -ltorch -lc10 -ltorch_cuda -lc10_cuda

# Librerías adicionales del sistema
LDLIBS += -lpthread -ldl -lrt

# Si se compila con GCC, a veces se necesita explícitamente libstdc++fs
# (en C++17, algunos métodos de filesystem)
LDLIBS += -lstdc++fs

# ----------------------------------------------------------------------------
# 4. OPCIONES DE ENLACE ESTÁTICO VS DINÁMICO
# ----------------------------------------------------------------------------
# Por defecto se usa enlace dinámico (shared). Para enlace estático (todo en uno),
# descomentar la siguiente línea y añadir -static, pero esto requiere que todas
# las bibliotecas estén disponibles como estáticas (.a) y puede causar problemas.
# Si se desea estático, se debe cambiar LDLIBS y añadir --whole-archive.
# NOTA: El enlace estático completo es complejo y no se recomienda.
# STATIC_LINK := -static

# ----------------------------------------------------------------------------
# 5. ARCHIVOS FUENTE Y OBJETIVOS
# ----------------------------------------------------------------------------
TARGET := loader_cpp
SOURCES := loader.cpp
OBJECTS := $(SOURCES:.cpp=.o)

# ----------------------------------------------------------------------------
# 6. REGLAS DE COMPILACIÓN
# ----------------------------------------------------------------------------
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $^ $(LDLIBS) -o $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# ----------------------------------------------------------------------------
# 7. REGLAS AUXILIARES
# ----------------------------------------------------------------------------
clean:
	rm -f $(OBJECTS) $(TARGET)

distclean: clean
	rm -f loader.cpp  # Opcional: elimina el generado si existe

# Ejecutar el binario (requiere que el listener esté activo)
run: $(TARGET)
	./$(TARGET)

# Mostrar la configuración actual
info:
	@echo "TORCH_DIR = $(TORCH_DIR)"
	@echo "CXX       = $(CXX)"
	@echo "CXXFLAGS  = $(CXXFLAGS)"
	@echo "LDFLAGS   = $(LDFLAGS)"
	@echo "LDLIBS    = $(LDLIBS)"
	@echo "TARGET    = $(TARGET)"

# Ayuda
help:
	@echo "Opciones del Makefile:"
	@echo "  make          : compila el ejecutable"
	@echo "  make clean    : elimina objetos y ejecutable"
	@echo "  make run      : compila y ejecuta"
	@echo "  make info     : muestra la configuración actual"
	@echo "  make TORCH_DIR=/ruta : especifica la ubicación de LibTorch"
	@echo "  make help     : muestra este mensaje"

# ----------------------------------------------------------------------------
# 8. COMPROBACIONES ADICIONALES
# ----------------------------------------------------------------------------
# Se verifica que el archivo fuente exista antes de compilar
$(SOURCES):
	@echo "Error: No se encuentra $(SOURCES). Asegúrate de que loader.cpp existe."
	@exit 1

# ----------------------------------------------------------------------------
# 9. REGLA PARA COMPILAR CON CLANG (OPCIONAL)
# ----------------------------------------------------------------------------
# Si se prefiere clang, se puede descomentar y ajustar.
# CXX := clang++
# CXXFLAGS += -stdlib=libc++  # Clang necesita esto a veces

.PHONY: all clean distclean run info help

