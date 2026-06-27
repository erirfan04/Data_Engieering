{% snapshot orders_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='order_id',
      strategy='timestamp',
      updated_at='order_date'
    )
}}

SELECT * FROM {{ source('raw', 'orders') }}

{% endsnapshot %}