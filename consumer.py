import pika
import os

def generar_recibo(ch, method, properties, body):
    mensaje = body.decode()
    print(f" [x] Recibido: {mensaje}")
    
    # Creamos el nombre del archivo basado en el contenido (o un timestamp)
    nombre_archivo = "ultimo_recibo.txt"
    
    with open(nombre_archivo, "w") as f:
        f.write("==============================\n")
        f.write("      RECIBO DE INSCRIPCIÓN   \n")
        f.write("==============================\n")
        f.write(f"Detalles: {mensaje}\n")
        f.write("Estado: PROCESADO EXITOSAMENTE\n")
        f.write("==============================\n")
    
    print(f" [v] Recibo generado en: {os.path.abspath(nombre_archivo)}")
    # Confirmar a RabbitMQ que el mensaje fue procesado
    ch.basic_ack(delivery_tag=method.delivery_tag)

def iniciar_consumidor():
    try:
        # Usa 'localhost' o la IP que configuramos antes
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        channel = connection.channel()

        channel.queue_declare(queue='examen_queue')
        print(' [*] Esperando mensajes para generar recibos. Para salir presiona CTRL+C')

        channel.basic_consume(queue='examen_queue', on_message_callback=generar_recibo)
        channel.start_consuming()
    except Exception as e:
        print(f" [!] Error en el consumidor: {e}")

if __name__ == '__main__':
    iniciar_consumidor()