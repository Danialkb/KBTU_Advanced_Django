"""changes

Revision ID: 0625e0465f7a
Revises: c04675f0e0be
Create Date: 2024-04-13 18:58:43.262184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0625e0465f7a'
down_revision: Union[str, None] = 'c04675f0e0be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crypto_trade', sa.Column('currency', sa.String(), nullable=False))
    op.drop_column('crypto_trade', 'purchase_currency')
    op.drop_column('crypto_trade', 'sold_currency')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crypto_trade', sa.Column('sold_currency', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('crypto_trade', sa.Column('purchase_currency', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('crypto_trade', 'currency')
    # ### end Alembic commands ###