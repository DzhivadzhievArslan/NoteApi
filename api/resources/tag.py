from api import Resource, abort, reqparse, auth
from api.models.tag import TagModel
from api.schemas.tag import TagSchema, TagRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, use_kwargs, doc
from webargs import fields

# language=YAML <-- оставил для примера
"""
Get User by id
---
tags:
    - Tags
parameters:
     - in: path
       name: tag_id
       type: integer
       required: true
       default: 1
responses:
   200:
       description: A single tag item
       schema:
           id: Tag
           properties:
               id:
                   type: integer
                   description: tag id
                   default: 1
               username:
                   type: string
                   description: The name of the tag
                   default: Steven Wilson
               is_staff:
                   type: boolean
                   description: tag
                   default: false
               role:
                   type: string
                   description: tag role
                   default: simple_tag
"""


@doc(tags=['Tags'])
class TagsResource(MethodResource):
    @marshal_with(TagSchema)
    @doc(summary="Get tag by id")
    def get(self, tag_id):
        tag = TagModel.query.get(tag_id)
        if not tag:
            abort(404, error=f"Tag with id={tag_id} not found")
        return tag, 200

    # @auth.login_required(role="admin")
    # @doc(summary="Edit tag by id")
    # @use_kwargs({"username": fields.Str(), "role": fields.Str()})
    # @marshal_with(TagSchema)
    # @doc(responses={401: {"description": "Not authorization"}})
    # @doc(responses={404: {"description": 'Tag not found'}})
    # @doc(security=[{"basicAuth": []}])
    # def put(self, tag_id, **kwargs):
    #     tag = TagModel.query.get(tag_id)
    #     if not tag:
    #         abort(404, error=f"tag with id={tag_id} not found")
    #     tag.username = kwargs.get("username") or tag.username
    #     tag.role = kwargs.get("role") or tag.role
    #     tag.save()
    #     return tag, 200
    #
    # @auth.login_required(role="admin")
    # @doc(summary='Delete tag by id')
    # @doc(responses={401: {"description": "Not authorization"}})
    # @doc(responses={404: {"description": "Not found"}})
    # @marshal_with(TagSchema)
    # @doc(security=[{"basicAuth": []}])
    # def delete(self, tag_id):
    #     tag = TagModel.query.get(tag_id)
    #     if not tag:
    #         abort(404, error=f"Tag with id:{tag_id} not found")
    #     tag.delete()
    #     return tag, 200


@doc(tags=['Tags'])
class TagsListResource(MethodResource):
    @marshal_with(TagSchema(many=True))
    @doc(summary="Get all Tags")
    def get(self):
        tags = TagModel.query.all()
        return tags, 200

    @doc(summary="Create new Tag")
    @marshal_with(TagSchema, code=201)
    @use_kwargs({"name": fields.Str(required=True)})
    def post(self, **kwargs):
        tag = TagModel(**kwargs)
        tag.save()
        return tag, 201
