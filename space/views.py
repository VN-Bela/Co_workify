from typing import Any
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    View,
)
from .models import WorkspaceImage, Workspace, SpaceCategory
from .forms import Workspace_Form, SpaceImage

# Create your views here.


class Home(TemplateView):
    template_name = "space/index.html"


class AboutView(TemplateView):
    template_name = "space/about.html"


class ContactView(TemplateView):
    template_name = "space/contact.html"


class PriceView(View):
    template_name = "space/price.html"
    def get(self,request):
        workspace_details=Workspace.objects.all()
        space_details=SpaceCategory.objects.all()
        WorkspaceImage_details=WorkspaceImage.objects.all()
        role=request.user.role if request.user.is_authenticated else None
        context={"workspace_details": workspace_details,"space_details":space_details,"WorkspaceImage_details":WorkspaceImage_details,"role":role}
        return render(request,self.template_name,context)

    def post(self,request):
        #address = request.POST["address"]
        space = request.POST["space"]
        # workspace_details=Workspace.objects.filter(address=address)
        space_details=SpaceCategory.objects.all()
        WorkspaceImage_details=WorkspaceImage.objects.all()
        # if address:
        #     WorkspaceImage_details = WorkspaceImage_details.filter(workspace_name__address=address)
        if space:
            WorkspaceImage_details = WorkspaceImage_details.filter(category__pk=space)
        role=request.user.role if request.user.is_authenticated else None
        context={"space_details":space_details,"WorkspaceImage_details":WorkspaceImage_details,"role":role}
        return render(request,self.template_name,context)

class GallaryView(ListView):
    model = WorkspaceImage
    template_name = "space/gallary.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = SpaceCategory.objects.all()
        return context


class RetriveWorkspace(DetailView):
    model = Workspace
    template_name = "space/workspace.html"
    form = SpaceImage()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        images = WorkspaceImage.objects.filter(workspace_name=self.object)
        context["images"] = images
        return context


class SpaceImageView(CreateView):
    model = WorkspaceImage
    # template_name = "space/index.html"
    form_class = SpaceImage

    def form_valid(self, form):
        self.pk = self.kwargs.get("pk")  # Retrieve pk from URL kwargs
        workspace_obj = Workspace.objects.get(pk=self.pk)
        form.instance.workspace_name = workspace_obj
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.request.META.get("HTTP_REFERER")


class DeleteImageview(DeleteView):
    model = WorkspaceImage
    template_name = "space/delete.html"
    # success_url= reverse_lazy("SpaceImageView")
    # after delete  content page stay same page

    def get_success_url(self) -> str:
        workspace_id = self.kwargs["workspace_id"]
        return reverse_lazy("RetriveWorkspace", kwargs={"pk": workspace_id})
        # return redirect(self.request.path)


class OrganizeView(TemplateView):
    template_name = "space/application.html"

    def get_context_data(self, **kwargs: Any):
        data = super().get_context_data(**kwargs)
        image_pk = kwargs.get("image_pk")
        # image = WorkspaceImage.objects.filter(pk=image_pk).first()
        image = get_object_or_404(WorkspaceImage, pk=image_pk)
        data["amount"] = image.get_amount()
        data["Adv_amount"] = image.get_amount() / 2
        data["seller"] = image.get_seller_name()
        data["address"] = image.workspace_name.address
        data["workspace_name"] = image.workspace_name.workspace_name
        data["seller_email"] = image.workspace_name.user.email
        user = self.request.user
        data["buyer"] = user.first_name + " " + user.last_name
        data["image_pk"] = image_pk
        return data
