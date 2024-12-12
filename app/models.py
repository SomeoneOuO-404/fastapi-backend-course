from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class User(Base):
    __tablename__ = "users"
    
    # 設定 id 欄位，並設為主鍵
    id = Column(Integer, primary_key=True, index=True)  
    
    # 設定 username 欄位，並加上 unique 和 nullable 限制
    username = Column(String(50), unique=True, nullable=False)
    
    # 設定 password 欄位
    password = Column(String(100), nullable=False)  # 密碼欄位通常需要適當加密
    
    # 設定 email 欄位，並加上 unique 和 nullable 限制
    email = Column(String(100), unique=True, nullable=False)
