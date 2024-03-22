class Parent:
    parent_member = 1

    def parent_method(self) -> None:
        print("나? 부모 메소드")


class Child(Parent):

    def child_method(self) -> None:
        print("나? 자식 메소드")


class ExternalClass:
    def external_method(self) -> None:
        print("나? 외부 클래스 메소드")


class ExternalClass2:
    def external_method(self) -> None:
        print("나? 외부 클래스 메소드2")


class CompositionClass:

    def __init__(self, exterenal_object: ExternalClass) -> None:
        self.external_object = exterenal_object

    def my_method(self) -> None:
        return self.external_object.external_method()


composition_object = CompositionClass(ExternalClass())
composition_object.my_method()
