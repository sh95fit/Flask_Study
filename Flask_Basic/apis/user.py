from flask_restx import Namespace, Resource, fields
from Flask_Basic.models.user import User as UserModel

ns = Namespace(
    'users',
    description='유저 관련 API',
)

user = ns.model('User', {
    'id': fields.Integer(required=True, description='유저 고유 번호'),
    'user_id': fields.String(required=True, description='유저 아이디'),
    'user_name': fields.String(required=True, description='유저 이름')
    # 실제로는 패스워드 정보도 있지만 프론트엔드에 노출시키지 않기 위해 숨김 - 모델을 정의해서 활용하는 이유! 필요한 값만 표시 가능!
})


# /api/users  (복수)
@ns.route('')
class UserList(Resource):
    @ ns.marshal_list_with(user, skip_none=True)
    def get(self):
        '''유저 복수 조회'''
        data = UserModel.query.all()
        return data


# /api/users/1 (단수)
@ns.route('/<int:id>')
@ns.param('id', '유저 고유 번호')
class User(Resource):
    @ ns.marshal_list_with(user, skip_none=True)
    def get(self, id):
        '''유저 단수 조회'''
        data = UserModel.query.get_or_404(id)
        return data
