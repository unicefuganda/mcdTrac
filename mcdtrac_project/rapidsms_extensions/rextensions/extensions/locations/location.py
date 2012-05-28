from django.db import models
#from rapidsms.contrib.locations.models import Location

class CodedLocation(models.Model):
    """
    Location - the main concept of a location.  Currently covers MOHSW, Regions, Districts and Facilities.
    This could/should be broken out into subclasses.
    """
    code = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

#    def set_parent(self, parent):
#        if hasattr(self,'tree_parent'):
#            self.tree_parent = parent
#        else:
#            self.parent = parent
#        self.save()
#
#    @property
#    def tree_parent(self):
#        """ This signature gets overriden by mptt when mptt is used """
#        return self.parent
#
#    @tree_parent.setter
#    def tree_parent(self, value):
#        """ This signature gets overriden by mptt when mptt is used """
#        self.parent = value
#
#    def get_children(self):
#        """ This signature gets overriden by mptt when mptt is used """
#        from rapidsms.contrib.locations.models import Location
#        return Location.objects.filter(parent_id=self.id, is_active=True).order_by('name')
#
#    def get_descendants(self, include_self=False):
#        """ This signature gets overriden by mptt when mptt is used
#        It must return a queryset
#        """
#        from rapidsms.contrib.locations.models import Location
#        def _get_descendent_pks(node):
#            pks = []
#            for c in node.get_children():
#                pks.append(c.pk)
#                pks.extend(_get_descendent_pks(c))
#            return pks
#        pks = _get_descendent_pks(self)
#        if include_self:
#            pks.append(self.pk)
#        ret = Location.objects.filter(id__in=pks, is_active=True)
#        return ret
#
#    def get_descendants_plus_self(self):
#        # utility to facilitate calling function from django template
#        return self.get_descendants(include_self=True)
#
#    def peers(self):
#        from rapidsms.contrib.locations.models import Location
#        # rl: is there a better way to do this?
#        if 'mptt' in settings.INSTALLED_APPS:
#            return Location.objects.filter(tree_parent=self.tree_parent, is_active=True).order_by('name')
#        return Location.objects.filter(parent_id=self.parent_id, is_active=True).order_by('name')
#
#    def deprecate(self, new_code=None):
#        """
#        Deprecates a location, by changing the code and deactivating it.
#        """
#        if new_code is None:
#            new_code = "deprecated-%s-%s" % (self.code, uuid.uuid4())
#        self.code = new_code
#        self.is_active = False
#        self.save()
