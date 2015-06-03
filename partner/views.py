from oscar.apps.partner import strategy, availability



class Selector(object):
    """
    Selector maravatio, no requiere inventario, no inlcute impuestos
    """

    def strategy(self):
        return THMStrategy()


class NoStockRequired(object):

    def availability_policy(self, product, stockrecord):
        print 'en estrategia'
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


class THMStrategy(strategy.UseFirstStockRecord, NoStockRequired, strategy.NoTax, strategy.Structured):