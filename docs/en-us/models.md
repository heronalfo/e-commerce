1. **Product**:
   - `id`: Unique identifier for the product (primary key)
   - `name`: Product name
   - `description`: Product description
   - `price`: Product price
   - `discount_price`: Discounted price (optional)
   - `category`: Foreign key to the product's category
   - `brand`: Product brand (optional)
   - `stock_quantity`: Product stock quantity
   - `image_url`: Product image URL (optional)
   - `date_added`: Date the product was added to the system

2. **Category**:
   - `id`: Unique identifier for the category (primary key)
   - `name`: Category name
   - `description`: Category description (optional)

3. **Customer**:
   - `id`: Unique identifier for the customer (primary key)
   - `first_name`: Customer's first name
   - `last_name`: Customer's last name
   - `email`: Customer's email address
   - `phone_number`: Customer's phone number (optional)
   - `address`: Customer's address (optional)
   - `date_registered`: Date the customer registered
   - `name`: Customer's name (optional)
   - `about`: Customer description (optional)
   - `cpf`: Customer's CPF (optional)
   - `cep`: Customer's Brazilian locality (optional)
   - `number`: Customer's number (optional)
   - `address`: Customer's address (optional)
   - `is_seller`: Indicates if the customer is a seller (optional)

4. **Order**:
   - `id`: Unique identifier for the order (primary key)
   - `customer`: Foreign key to the customer who placed the order
   - `date_ordered`: Date the order was placed
   - `complete`: Indicator if the order is complete or not
   - `transaction_id`: Transaction ID (for payment systems)
   - `shipping_address`: Order shipping address (optional)
   - `billing_address`: Order billing address (optional)
   - `payment_method`: Payment method used (optional)

5. **OrderItem**:
   - `id`: Unique identifier for the order item (primary key)
   - `product`: Foreign key to the product in the order
   - `order`: Foreign key to the order to which this item belongs
   - `quantity`: Quantity of the product in the order
   - `unit_price`: Unit price of the product at the time of the order
   - `total_price`: Total price for this item in the order

6. **Payment**:
   - `id`: Unique identifier for the payment (primary key)
   - `customer`: Foreign key to the customer who made the payment
   - `order`: Foreign key to the order associated with the payment
   - `payment_date`: Date the payment was made
   - `amount`: Amount paid
   - `payment_method`: Payment method used
   - `transaction_id`: Transaction ID (optional)

7. **Review**:
   - `id`: Unique identifier for the review (primary key)
   - `product`: Foreign key to the reviewed product
   - `customer`: Foreign key to the customer who wrote the review
   - `rating`: Numerical rating of the product (e.g., from 1 to 5)
   - `comment`: Comment written by the customer
   - `date_added`: Date the review was added

8. **Shipping**:
   - `id`: Unique identifier for the shipping (primary key)
   - `order`: Foreign key to the order associated with the shipping
   - `customer`: Foreign key to the customer who placed the order
   - `shipment_date`: Date the order was shipped
   - `tracking_number`: Shipping tracking number
   - `shipping_method`: Shipping method used