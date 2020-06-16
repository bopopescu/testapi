from  flask import jsonify
from flask_restful import Resource,reqparse
from db import query

class Emp(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('empno',type=int,required=True,help='empno cannot be left blank')
        data=parser.parse_args()
        try:
            return query(f"""select * from testapi.emp where empno={data['empno']};""")
        except:
            return{"message":"there was an error connecting to emp table"},500

    def post(self):
         parser=reqparse.RequestParser()
         parser.add_argument('empno',type=int,required=True,help='empno cannot be left blank')
         parser.add_argument('ename',type=str,required=True,help='ename cannot be left blank')
         parser.add_argument('job',type=str,required=True,help='job cannot be left blank')
         parser.add_argument('mgr',type=int,required=True,help='mgr cannot be left blank')
         parser.add_argument('hiredate',type=str,required=True,help='hiredate cannot be left blank')
         parser.add_argument('sal',type=str,required=True,help='sal cannot be left blank')
         parser.add_argument('comm',type=str)
         parser.add_argument('deptno',type=int,required=True,help='deptno cannot be left blank')
         data=parser.parse_args()
         try:
            x=query(f"""select * from testapi.emp where empno={data['empno']};""",return_json=False)
            if len(x)>0:return {"message":"An emp with that info already exists"},400

         except:
            return{"message":"there was an error inserting to emp table"},500
         if data['comm']!=None:
            try:
                query(f"""insert into testapi.emp values({data['empno']},
                                                             '{data['ename']}',
                                                             '{data['job']}',
                                                              {data['mgr']},
                                                              '{data['hiredate']}',
                                                              '{data['sal']}',
                                                              '{data['comm']}',
                                                              {data['deptno']})""")
            except:
                return{"message":"there was an error insertting to emp table"},500
            return {"message":"success inserted."},201
         else:
             try:
                query(f"""insert into testapi.emp(empno,ename,job,mgr,hiredate,sal,deptno) values({data['empno']},
                                                             '{data['ename']}',
                                                             '{data['job']}',
                                                              {data['mgr']},
                                                              '{data['hiredate']}',
                                                              '{data['sal']}',
                                                              {data['deptno']})""")
             except:
                return{"message":"there was an error insertting to emp table"},500
             return {"message":"success inserted."},201
             


