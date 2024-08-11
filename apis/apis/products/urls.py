from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()

router.register(prefix="products", viewset=ProductViewSet, basename="Products")

urlpatterns = router.urls


# from .views import (
#     ProductListCreateAPIView,
#     ProductRetrieveUpdateDeleteAPIView,
#     ProductListCreateGAPIView,
#     ProductUpdateRetrieveDestoryGAPIView,
# )


# ApiView and GenericView
# urlpatterns = [
#     path(
#         route="apiView/products/",
#         view=ProductListCreateAPIView.as_view(),
#         name="apiView product-List-create",
#     ),
#     path(
#         route="apiView/products/<id>/",
#         view=ProductRetrieveUpdateDeleteAPIView.as_view(),
#         name="apiView product-retrieve-update-destroy",
#     ),
#     path(
#         route="genericView/products/",
#         view=ProductListCreateGAPIView.as_view(),
#         name="Generic View product-list-create",
#     ),
#     path(
#         route="genericView/products/<slug:slug>",
#         view=ProductUpdateRetrieveDestoryGAPIView.as_view(),
#         name="Generic View product-retrieve-destory-update",
#     ),
#     # path(
#     #     route="genericView/products/create",
#     #     view=ProductCreateView.as_view(),
#     # ),
#     # path(
#     #     route="genericView/products/<slug>",
#     #     view=ProductRetrieve.as_view(),
#     # ),
#     # path(
#     #     route="genericView/products/<slug>/update",
#     #     view=ProductUpdate.as_view(),
#     # ),
# ]


# ApiView

# urlpatterns = [
#     path(route="apiView/products/", view=ProductListCreateAPIView.as_view()),
#     path(
#         route="apiView/products/<id>/",
#         view=ProductRetrieveUpdateDeleteAPIView.as_view(),
#     ),
#     path(
#         route="genericView/products/",
#         view=ProductListView.as_view(),
#     ),
#     path(
#         route="genericView/products/create",
#         view=ProductCreateView.as_view(),
#     ),
#     path(
#         route="genericView/products/<slug>",
#         view=ProductRetrieve.as_view(),
#     ),
#     path(
#         route="genericView/products/<slug>/update",
#         view=ProductUpdate.as_view(),
#     ),
# ]
