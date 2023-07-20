#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <netdb.h>

#define MAX_MESSAGE_LEN 1024

int main(int argc, char const* argv[]) {
    int status, valread, client_fd;
    struct sockaddr_in serv_addr;
    char domain[256];
    int port;
    char message[MAX_MESSAGE_LEN];
    char buffer[MAX_MESSAGE_LEN] = {0};

    printf("Enter the domain name: ");
    scanf("%s", domain);

    printf("Enter the port number: ");
    scanf("%d", &port);

    printf("Enter the message to send: ");
    fflush(stdout);
    getchar();
    fgets(message, sizeof(message), stdin);

    size_t len = strlen(message);
    if (len > 0 && message[len - 1] == '\n')
        message[len - 1] = '\0';

    if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

    struct addrinfo hints, *res;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    if (getaddrinfo(domain, NULL, &hints, &res) != 0) {
        fprintf(stderr, "Failed to get IP address for domain: %s\n", domain);
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    serv_addr.sin_addr = ((struct sockaddr_in*)res->ai_addr)->sin_addr;

    if ((status = connect(client_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }

    send(client_fd, message, strlen(message), 0);

    valread = read(client_fd, buffer, sizeof(buffer) - 1);
    if (valread < 0) {
        perror("read");
        close(client_fd);
        return -1;
    }
    buffer[valread] = '\0';
    printf("Received from server: %s\n", buffer);

    close(client_fd);
    freeaddrinfo(res);
    return 0;
}
