-- Stage table
CREATE TABLE user_stage (
    id VARCHAR(50),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50),
    birth_date DATE,
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(100),
    etl_load_date TIMESTAMP,
    CONSTRAINT pk_user_stage PRIMARY KEY (id)
);

-- Target table
CREATE TABLE user (
    id VARCHAR(50),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50),
    birth_date DATE,
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_user PRIMARY KEY (id)
);

-- Create index for better performance
CREATE INDEX idx_user_email ON user(email);
CREATE INDEX idx_user_name ON user(last_name, first_name);