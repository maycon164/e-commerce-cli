from core.discounts.discount_rule import Condition, Discount

#TODO: EXAMPLES OF CONDITIONS
#| Type           | Class                     | Description                                           |
#| -------------- | ------------------------- | ----------------------------------------------------- |
#| Total value    | `MinPurchaseCondition`    | Requires `purchase.total >= X`                        |
#| Localization   | `LocationCondition`       | Requires user or delivery country to be in a set      |
#| Partner        | `PartnerCompanyCondition` | Requires user to belong to a certain company or group |
#| First purchase | `FirstPurchaseCondition`  | True only if it's user's first order                  |
#| Device         | `DeviceCondition`         | E.g., only applies to app, mobile browser, etc.       |
#| Condition Type              | Purpose                                                                |
#| --------------------------- | ---------------------------------------------------------------------- |
#| `UserSegmentCondition`      | e.g., new users, loyal users, students                                 |
#| `TimeWindowCondition`       | Valid only within a certain time window (Black Friday, weekends, etc.) |
#| `CategoryCondition`         | Applies only to certain product categories                             |
#| `CartContainsItemCondition` | Requires a specific product (or tag) in the cart                       |
#| `MaxUsagePerUserCondition`  | Only usable once or N times per user                                   |
# TODO: how a compose condition could be implementhed like MinPurchaseCondition and DeviceCondition

#TODO: EXAMPLE OF DISCOUNTS
#| Discount Type          | Example                                       |
#| ---------------------- | --------------------------------------------- |
#| `PercentageDiscount`   | 15% off                                       |
#| `FreeShippingDiscount` | waives shipping fees                          |
#| `BuyXGetYDiscount`     | Buy 2, get 1 free                             |
#| `TieredDiscount`       | e.g., 5% off up to \$100, 10% off above \$100 |

# TODO: ADD RULES
#| Feature                    | Description                                   |
#| -------------------------- | --------------------------------------------- |
#| **Coupon expiration date** | `valid_until` date on the coupon              |
#| **Max total uses**         | Coupon can be used only X times platform-wide |
#| **Max per user**           | Coupon can be used only once per user         |
#| **Combination rules**      | Can it be combined with other coupons/promos? |

### MORE CHALLENGES
#Tokenized coupons: some codes are randomly generated, per-user, or one-time.
#Validate ownership: user must “own” the coupon.
#Prevent replay: avoid re-applying expired/used coupons.

class Coupon:

    code: str

    def __init__(self, code: str, condition: Condition, discount: Discount):
        self.code = code
        self.condition = condition
        self.discount = discount