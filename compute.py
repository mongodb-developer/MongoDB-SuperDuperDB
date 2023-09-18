from superduperdb import superduper 
from sentence_transformers import SentenceTransformer

model = superduper(
    SentenceTransformer('all-MiniLM-L6-v2')
)

model.predict(
    X='input_col',
    db=db,
    select=Collection(name='test_documents')
)
