from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class NeodataBypassServer(BaseHTTPRequestHandler):
    def do_POST(self):
        self.process_request()
        
    def do_GET(self):
        self.process_request()

    def process_request(self):
        # Responder con éxito HTTP 200 y formato JSON
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        
        # Tu JSON real y estructurado bit por bit (Modo Universal sin logotipo)
        response_data = {
            "accessToken": "ya29.a0AT3oNZ9YCU3HpV22vtBhm8F4eMNvXrYX1hq0OVKVxHO0dlqWI2PgDXMgs1dmoDjTK4v4imPz1lEECK3bgi4ixAKvT7p1Ip0Rz9MWgQayUX0aWGqgTpHnXJ9e-jJ40NM1k957dBz5oELtDQzw-MHZNx-H8SfU5vj5m8lE82oNEtPOK7y9-xpgKcnyJmgYF-jMJnHz3KoaCgYKAa8SARMSFQHGX2MiohyKRU0pvuAt7hxsl6vIJQ0206",
            "token": "",
            "name": "TECSI Ingenieria",
            "email": "tecsiingenieria@gmail.com",
            "picture": "",  # Forzado a vacío para eliminar el logotipo en todas las computadoras
            "expiresIn": 31536000,
            "oauthExpireIn": 31536000,
            "fechaVigencia": "2029-12-31",
            "numeroLicencia": 85412,
            "razonSocial": "Tecsi Ingenieria",
            "sesion": 303873024228148564,
            "otraSesionActiva": False,
            "caducoSesion": False,
            "tokenCaducado": False,
            "noTieneVigencia": False,
            "cambioIp": False,
            "idUsuario": 85412,
            "idUsuarioAdmin": 85412,
            "emailAdmin": "",
            "idEmpresa": 85412,
            "licenciaEstudiantil": False,
            "mensajeComunicado": "",
            "idLicencia": 85412,
            "Offline": False,
            "admin": False,
            "permiteOffline": True,
            "limitePptoPu": {
                "TipoLicencia": "Versión Corporativa",
                "TotalConceptos": 999999,
                "TotalInsumos": 999999,
                "TotalMaestrosLibresEscritura": 999999,
                "TotalPptoCompartidos": 999999,
                "AlmacenExtraInsumos": 999999,
                "AlmacenExtraConceptos": 999999,
                "SoloNube": False,
                "Errores": {
                    "error": "",
                    "errorDescripcion": ""
                }
            },
            "errores": {
                "error": "",
                "errorDescripcion": ""
            }
        }
        
        # Convertir a cadena de texto y enviar a Neodata
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=NeodataBypassServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor Local de Licencias Neodata 25.9 activo en el puerto {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
