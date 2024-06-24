1. **Product (Produto)**:
   - `id`: Identificador único do produto (chave primária)
   - `name`: Nome do produto
   - `description`: Descrição do produto
   - `price`: Preço do produto
   - `discount_price`: Preço com desconto (opcional)
   - `category`: Chave estrangeira para a categoria do produto
   - `brand`: Marca do produto (opcional)
   - `stock_quantity`: Quantidade em estoque do produto
   - `image_url`: URL da imagem do produto (opcional)
   - `date_added`: Data de adição do produto ao sistema

2. **Category (Categoria)**:
   - `id`: Identificador único da categoria (chave primária)
   - `name`: Nome da categoria
   - `description`: Descrição da categoria (opcional)

3. **Customer (Cliente)**:
   - `id`: Identificador único do cliente (chave primária)
   - `first_name`: Primeiro nome do cliente
   - `last_name`: Sobrenome do cliente
   - `email`: Endereço de e-mail do cliente
   - `phone_number`: Número de telefone do cliente (opcional)
   - `address`: Endereço do cliente (opcional)
   - `date_registered`: Data de registro do cliente

4. **Order (Pedido)**:
   - `id`: Identificador único do pedido (chave primária)
   - `customer`: Chave estrangeira para o cliente que fez o pedido
   - `date_ordered`: Data em que o pedido foi realizado
   - `complete`: Indicador se o pedido está completo ou não
   - `transaction_id`: ID da transação (para sistemas de pagamento)
   - `shipping_address`: Endereço de entrega do pedido (opcional)
   - `billing_address`: Endereço de faturamento do pedido (opcional)
   - `payment_method`: Método de pagamento utilizado (opcional)

5. **OrderItem (Item do Pedido)**:
   - `id`: Identificador único do item do pedido (chave primária)
   - `product`: Chave estrangeira para o produto no pedido
   - `order`: Chave estrangeira para o pedido ao qual este item pertence
   - `quantity`: Quantidade do produto no pedido
   - `unit_price`: Preço unitário do produto no momento do pedido
   - `total_price`: Preço total para este item no pedido

6. **Payment (Pagamento)**:
   - `id`: Identificador único do pagamento (chave primária)
   - `customer`: Chave estrangeira para o cliente que fez o pagamento
   - `order`: Chave estrangeira para o pedido associado ao pagamento
   - `payment_date`: Data em que o pagamento foi realizado
   - `amount`: Valor pago
   - `payment_method`: Método de pagamento utilizado
   - `transaction_id`: ID da transação (opcional)

7. **Review (Avaliação)**:
   - `id`: Identificador único da avaliação (chave primária)
   - `product`: Chave estrangeira para o produto avaliado
   - `customer`: Chave estrangeira para o cliente que fez a avaliação
   - `rating`: Avaliação numérica do produto (por exemplo, de 1 a 5)
   - `comment`: Comentário escrito pelo cliente
   - `date_added`: Data em que a avaliação foi adicionada

8. **Shipping (Envio)**:
   - `id`: Identificador único do envio (chave primária)
   - `order`: Chave estrangeira para o pedido associado ao envio
   - `customer`: Chave estrangeira para o cliente que fez o pedido
   - `shipment_date`: Data de envio do pedido
   - `tracking_number`: Número de rastreamento do envio
   - `shipping_method`: Método de envio utilizado