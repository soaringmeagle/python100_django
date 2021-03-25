from bpmappers.djangomodel import ModelMapper
from bpmappers import RawField
from polls.models import Subject, Teacher, User


class SubjectMapper(ModelMapper):
    isHot = RawField('is_hot')

    class Meta:
        model = Subject
        exclude = ('is_hot',)
