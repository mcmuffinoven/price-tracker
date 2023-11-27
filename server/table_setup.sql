create table if not exists price_tracker(
    id serial primary key not null,
    category varchar not null,
    product_name varchar unique not null,
    starting_product_price float not null,
    current_product_price float not null,
    lowest_product_price float not null,
    lowest_product_price_date timestamp not null,
    tracked_since_date timestamp not null,
    product_link text not null,
    sale_bool boolean not null
);

insert into price_tracker (
        category,
        product_name,
        starting_product_price,
        current_product_price,
        lowest_product_price,
        lowest_product_price_date,
        tracked_since_date,
        product_link,
        sale_bool
    )
values (
        'Tech',
        'Logitec G502 X',
        472.00,
        200.00,
        104.00,
        '2023-11-19',
        '2023-11-19',
        'https://www.bestbuy.ca/en-ca/product/insignia-32-1080p-fhd-led-smart-tv-ns-32f202ca23-fire-tv-edition-2022-only-at-best-buy/16016210',
        false
    );

insert into price_tracker (
        category,
        product_name,
        starting_product_price,
        current_product_price,
        lowest_product_price,
        lowest_product_price_date,
        tracked_since_date,
        product_link,
        sale_bool
    )
values (
        'Tech',
        'Asus OLED Monitor',
        2010.00,
        2003.21,
        1999.00,
        '2012-04-23',
        '2012-04-20',
        'https://www.bestbuy.ca/en-ca/product/insignia-32-1080p-fhd-led-smart-tv-ns-32f202ca23-fire-tv-edition-2022-only-at-best-buy/16016210',
        true
    );

insert into price_tracker (
        category,
        product_name,
        starting_product_price,
        current_product_price,
        lowest_product_price,
        lowest_product_price_date,
        tracked_since_date,
        product_link,
        sale_bool
    )
values (
        'Fashion',
        'Ski Goggles',
        200.00,
        200.00,
        192.00,
        '2012-04-23',
        '2012-03-22',
        'https://www.bestbuy.ca/en-ca/product/insignia-32-1080p-fhd-led-smart-tv-ns-32f202ca23-fire-tv-edition-2022-only-at-best-buy/16016210',
        false
    );

insert into price_tracker (
        category,
        product_name,
        starting_product_price,
        current_product_price,
        lowest_product_price,
        lowest_product_price_date,
        tracked_since_date,
        product_link,
        sale_bool
    )
values (
        'Grocery',
        'Coffee',
        67.00,
        65.3,
        33,
        '2012-04-23',
        '2012-01-20',
        'https://www.bestbuy.ca/en-ca/product/insignia-32-1080p-fhd-led-smart-tv-ns-32f202ca23-fire-tv-edition-2022-only-at-best-buy/16016210',
        true
    );

insert into price_tracker (
        category,
        product_name,
        starting_product_price,
        current_product_price,
        lowest_product_price,
        lowest_product_price_date,
        tracked_since_date,
        product_link,
        sale_bool
    )
values (
                'Cosmetics',
                'Avene Cream',
                22.23,
                22.23,
                11,
                '2012-04-23',
                '2012-03-20',
                'https://www.bestbuy.ca/en-ca/product/insignia-32-1080p-fhd-led-smart-tv-ns-32f202ca23-fire-tv-edition-2022-only-at-best-buy/16016210',
                false
    );
