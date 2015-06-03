from oscar.apps.partner.strategy import Selector as CoreSelector, UseFirstStockRecord, NoTax, Structured
from oscar.apps.partner import availability


class Selector(CoreSelector):
    """
    Selector maravatio, no requiere inventario, no inlcute impuestos
    """

    def strategy(self, request=None, user=None, **kwargs):
        return THMStrategy()


class NoStockRequired(object):

    def availability_policy(self, product, stockrecord):
        return availability.Available()
        # if not stockrecord:
        #     return availability.Unavailable()
        # if not product.get_product_class().track_stock:
        #     return availability.Available()
        # else:
        #     return availability.StockRequired(
        #         stockrecord.net_stock_level)

    def parent_availability_policy(self, product, children_stock):

        return availability.Available()
        # # A parent product is available if one of its children is
        # for child, stockrecord in children_stock:
        #     policy = self.availability_policy(product, stockrecord)
        #     if policy.is_available_to_buy:
        #         return availability.Available()
        # return availability.Unavailable()


class THMStrategy(UseFirstStockRecord, NoStockRequired, NoTax, Structured):
    pass
